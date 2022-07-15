# Entrega1LezanBlanc
primera entrega proyecto final 
Para este proyecto nos basamos en una empresa exportadora de vinos, sobre la cual creamos la Web Django con patrón MVT.
Los models se crearon en base a los clientes, las bodegas proveedoras y los vinos que se comercializan. 
En función de estos models, creamos los templates de formularios con los cuales solicitar:
Para Clientes:  nombre e email
Para Vinos: nombre, varietal, bodega.
Para Bodega: nombre, email, país.	
Y que luego los devuelva en una tabla. 
En el caso de Clientes, incluimos un formulario de búsqueda y un template que muestre los resultados de esta búsqueda. 
Para darle funcionalidad, creamos las views. En primer lugar, una por cada html (inicio, bodega, vino y clientes) y luego las views de los formularios. Primero creamos las views de los forms: 
 Para el caso de ingresar por POST, indicamos que la información que ingrese, luego de pasar por la validación de Django, se limpie el form y la información se guarde como diccionario. Se creará un objeto de mi clase Bodega y se guardará. Al finalizar nos llevara a la pagina de inicio. 
Si la información nos llegara a través de GET, se renderizará y enviara como diccionario para ser utilizado por el template. 
El view del form de búsqueda, creamos dos, el de búsqueda Cliente simple rederizado y el de buscar, que funcione a través de Get, para que busque dentro de mis objetos cliente según el request, que brinde una respuesta antes de dar el resultado y que, en caso de encontrarlo muestre el resultado y para el caso de no tener una respuesta de búsqueda, que muestre el mensaje “Error, no se ingreso un cliente”.
