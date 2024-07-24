from crea_informes import crearinformes
from leearchivos import leerarchivos
from envio_mail import camp_alumnos, camp_errores, camp_secciones

leerarchivos()
crearinformes()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
camp_errores(1)
camp_secciones(1)
camp_alumnos(1)
