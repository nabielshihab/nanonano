import numpy as np
import matplotlib.pyplot as plt


def project_to_slice(position, p1, p2):
    '''
    Proyeksi data spasial 2D (x, y) ke satu garis yang 
    dibentuk oleh dua titik p1 dan p2, mengembalikan 
    output berupa matriks ukuran (1, n) yang menggambarkan
    posisi titik2 spasial di 2D di sepanjang garis yang dibentuk 
    p1 dan p2.
    
    arguments:
    --p1 & p2
        Titik (x,y) dari satu titik yang akan membentuk garis
        dalam numpy array -> p1 = np.array([x, y]), dengan ukuran 
        (2,)
    --position
        numpy array dari posisi spasial suatu titik
        ukuran (2, n), row 1 berisi koordinat x, row 2 berisi koordinat y
        dengan n = banyak titik
        contoh :
            position = np.array([[x1, x2, .., xn], 
                                 [y1, y2, .., yn]])
    '''
    ## Vektor lokasi dari garis slice
    v_slice = p2-p1
    v_slice = v_slice[np.newaxis, ...]
    
    ## vektor lokasi titik episenter terhadap titik p1
    v_epi = position - p1[:, None]
    
    ## lokasi titik (x, y) hasil proyeksi
    new_x = v_slice.dot(v_epi) / (np.linalg.norm(v_slice))
    return new_x


def plot_slice(hipo, new_x, p1, p2, figsize=(10, 6)):
    '''
    hipo : matriks (3xn) berisi kordinat hiposenter 
    new_x : hasil proyeksi episenter ke garis slice
    p1, p2 : titik2 ujung garis
    '''
    
    plt.figure(figsize=figsize)

    plt.subplot(121)
    plt.scatter(hipo[0, :], hipo[1, :])
    plt.plot((p1[0], p2[0]), (p1[1], p2[1]), c='r', label='Slice')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Basemap')

    plt.subplot(122)
    plt.scatter(new_x, hipo[2, :])
    plt.gca().invert_xaxis()
    plt.title('Vertical Slice')
    plt.xlabel('Distance')