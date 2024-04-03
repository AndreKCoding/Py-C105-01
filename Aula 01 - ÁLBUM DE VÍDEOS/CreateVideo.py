import os
import cv2


path = "Imagens"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

first_frame = cv2.imread(images[0])

altura, largura, canais = first_frame.shape
tamanho = (largura, altura)
print(tamanho)

video = cv2.VideoWriter("Projeto.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, tamanho)

for i in range(count - 1):
    frame = cv2.imread(images[i])
    video.write(frame)

video.release()
print('Concluido!')
