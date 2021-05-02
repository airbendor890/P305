#include<math.h>
#include<TCanvas.h>
void hist_QA(){

	TCanvas* c= new TCanvas("c","plots",1200,1200);
	c->Divide(2,3);
	c->cd(1);
//////////////////////////////////////////////////////////////////////////////////
	double E_max,E_min=0;
	double tmp;



	ifstream file;
	file.open("data1.txt");
	while(file>>tmp){
		if(tmp<=E_min) E_min=tmp;
	}
	file.close();

	file.open("data1.txt");

	E_max=E_min;
	while(file>>tmp){
		if(tmp>=E_max) E_max=tmp;
	}
	file.close();

	TH1D* h1=new TH1D("h1","density of states;eigen value;density",100,E_min-2,E_max+2);
	file.open("data1.txt");

	while(file>>tmp){
		h1->Fill(tmp);
	}
	file.close();
	cout<<E_min<<"\t"<<E_max<<endl;
	h1->Draw();

///////////////////////////////////////////////////////////////////////////////////
	c->cd(2);
	E_max=0;E_min=0;

	file.open("data2.txt");
	while(file>>tmp){
		if(tmp<=E_min) E_min=tmp;
	}
	file.close();

	file.open("data2.txt");

	E_max=E_min;
	while(file>>tmp){
		if(tmp>=E_max) E_max=tmp;
	}
	file.close();

	TH1D* h2=new TH1D("h2","density of states;eigen value;density",100,E_min-2,E_max+2);
	file.open("data2.txt");

	while(file>>tmp){
		h2->Fill(tmp);
	}
	file.close();
	cout<<E_min<<"\t"<<E_max<<endl;
	h2->Draw();

///////////////////////////////////////////////////////////////////////////////////
	c->cd(3);
	E_max=0;E_min=0;

	file.open("data3.txt");
	while(file>>tmp){
		if(tmp<=E_min) E_min=tmp;
	}
	file.close();

	file.open("data3.txt");

	E_max=E_min;
	while(file>>tmp){
		if(tmp>=E_max) E_max=tmp;
	}
	file.close();

	TH1D* h3=new TH1D("h3","density of states;eigen value;density",100,E_min-2,E_max+2);
	file.open("data3.txt");

	while(file>>tmp){
		h3->Fill(tmp);
	}
	file.close();
	cout<<E_min<<"\t"<<E_max<<endl;
	h3->Draw();


///////////////////////////////////////////////////////////////////////////////////
	c->cd(4);
	E_max=0;E_min=0;

	file.open("data4.txt");
	while(file>>tmp){
		if(tmp<=E_min) E_min=tmp;
	}
	file.close();

	file.open("data4.txt");

	E_max=E_min;
	while(file>>tmp){
		if(tmp>=E_max) E_max=tmp;
	}
	file.close();

	TH1D* h4=new TH1D("h4","density of states;eigen value;density",100,E_min-2,E_max+2);
	file.open("data4.txt");

	while(file>>tmp){
		h4->Fill(tmp);
	}
	file.close();
	cout<<E_min<<"\t"<<E_max<<endl;
	h4->Draw();
///////////////////////////////////////////////////////////////////////////////////
	c->cd(5);
	E_max=0;E_min=0;

	file.open("data5.txt");
	while(file>>tmp){
		if(tmp<=E_min) E_min=tmp;
	}
	file.close();

	file.open("data5.txt");

	E_max=E_min;
	while(file>>tmp){
		if(tmp>=E_max) E_max=tmp;
	}
	file.close();

	TH1D* h5=new TH1D("h5","density of states;eigen value;density",100,E_min-2,E_max+2);
	file.open("data5.txt");

	while(file>>tmp){
		h5->Fill(tmp);
	}
	file.close();
	cout<<E_min<<"\t"<<E_max<<endl;
	h5->Draw();
//////////////////////////////////////////////////////////////////////////////////
	c->cd(6);
	E_max=0;E_min=0;

	file.open("data6.txt");
	while(file>>tmp){
		if(tmp<=E_min) E_min=tmp;
	}
	file.close();

	file.open("data6.txt");

	E_max=E_min;
	while(file>>tmp){
		if(tmp>=E_max) E_max=tmp;
	}
	file.close();

	TH1D* h6=new TH1D("h6","density of states;eigen value;density",100,E_min-2,E_max+2);
	file.open("data6.txt");

	while(file>>tmp){
		h6->Fill(tmp);
	}
	file.close();
	cout<<E_min<<"\t"<<E_max<<endl;
	h6->Draw();
///////////////////////////////////////////////////////////////////////////////////
}
