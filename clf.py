from torchvision import models, transforms
import torch
from PIL import Image
import time
def predict(image_path,option):
    if option =="resnet101":
        model = models.resnet101(pretrained=True)
    elif option =="resnet50":
        model = models.resnet50(pretrained=True)
    elif option == "densenet121":
        model = models.densenet121(pretrained=True)
    elif option == "shufflenet_v2_x0_5":
        model = models.shufflenet_v2_x0_5(pretrained=True)
    else:
        model = models.mobilenet_v2(pretrained=True)

    #https://pytorch.org/docs/stable/torchvision/models.html
    transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225]
    )])

    img = Image.open(image_path)
    batch_t = torch.unsqueeze(transform(img), 0)

    model.eval()
    t1 = time.time()
    out = model(batch_t)
    t2 = time.time()
    fps = round(float(1 / (t2 - t1)), 3)
    with open('imagenet_classes.txt') as f:
        classes = [line.strip() for line in f.readlines()]
    prob = torch.nn.functional.softmax(out, dim=1)[0] * 100
    _, indices = torch.sort(out, descending=True)
    return [(classes[idx], prob[idx].item()) for idx in indices[0][:5]],fps


