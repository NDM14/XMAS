from IPython.display import Image

richtige_laenge = 17

def trenn_die_listen(Liste1, Liste2):
    uneven =  [3, 123, 1897, 69]

    even = [10, 42, 120, 6, 12, 422]
    
    if Liste1 == even and Liste2 == uneven:
        return Image(url='Gutschein.png')
    else:
        return Image(url='https://media.tenor.com/UnpKBaEgD1sAAAAC/you-know-it-seems-like-something-still-not-right-kyle-broflovski.gif')
