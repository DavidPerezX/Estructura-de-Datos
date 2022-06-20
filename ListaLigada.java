
public class ListaLigada{
	
	//Propiedades
	private Elemento[] LL;
	private int tamano;
	private int tamanoMax;

	//Cosntructor
	public ListaLigada(double valor,int tamanoMax){
		this.LL = new Elemento[tamanoMax];
		this.LL[0] = new Elemento(valor,0,0);
		this.tamano = 1;
		this.tamanoMax = tamanoMax; 
	}

	public ListaLigada(int tamanoMax){
		this.LL = new Elemento[tamanoMax];
		this.tamano = 0;
		this.tamanoMax = tamanoMax; 
	}
	
	//Accesors
	public Elemento[] getElementos(){
		return LL;
	}
	public void setElementos(Elemento[] LL){
		this.LL=LL;
	}
	
	public int getTamano(){
		return tamano;
	}

	public void setTamano(int tamano){
		this.tamano=tamano;
	}

	public int getTamanoMax(){
		return tamanoMax;
	}

	public void setTamanoMax(int tamanoMax){
		this.tamanoMax=tamano;
	}

	//Funciones a programar
	public Boolean vacia(){
		return tamano==0;
	}

	public Boolean llena(){
		return tamano==tamanoMax;
	}

	public void insertar(int indice,double valor){
		if(llena()){
			System.out.println("La lista está llena");
		}
		else if(vacia()){
			Elemento e=new Elemento(valor,0,0);
			LL[tamano]=e;
			tamano++;
		}
		else{
			int i=0,indiceActual=LL[0].getIndice();
			while(indice!=indiceActual&&i<tamano){
				i++;
				indiceActual=LL[i].getIndice();
			}
			int aux;
			Boolean encontro=false;
			for(int j=0;j<tamanoMax&&!encontro;j++){
				for(int k=0;k<tamano;k++){
					if(LL[k].getIndice()==j){
						encontro=true;
					}	
				}
				
			}
			Elemento e=new Elemento(valor,tamano,LL[indiceActual].getSiguiente());
			LL[indiceActual].setSiguiente(tamano);
		}
	}
	public void insertar(double elemento,double valor){
		if(llena()){
			System.out.println("La lista está llena");
		}
		else if(vacia()){
			Elemento e=new Elemento(valor,0,0);
			LL[tamano]=e;
			tamano++;
		}
		else{
			indice=buscar(elemento);
			insertar(indice,valor);
		}
	}


} 