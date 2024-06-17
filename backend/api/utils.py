import torch
import torchvision


class CHDModelResnet(torch.nn.Module):
    def __init__(self, num_classes):
        super(CHDModelResnet, self).__init__()
        self.model = torchvision.models.resnet50(pretrained=True)
        num_ftrs = self.model.fc.in_features
        self.model.fc = torch.nn.Linear(in_features=num_ftrs, out_features=num_classes, bias=True)

        self.feature_map = {}

    def forward(self, x):
        self.feature_map['layer4'] = torch.nn.Sequential(*list(self.model.children())[:-2])(x)
        pred = self.model(x)

        return pred
    

def preparation():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    num_classes = 4
    resnet_weights_path = "/content/drive/MyDrive/CHD/best_model_resnet50_pretrained_new8_42.pth"
    resnet_model = CHDModelResnet(num_classes).to(device)
    resnet_model.load_state_dict(torch.load(resnet_weights_path))
    return resnet_model
