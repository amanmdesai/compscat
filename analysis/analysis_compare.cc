
//using namespace std;
void histocombo(TH1 *histo1,TH1 *histo2, const char* namecan, const char* xaxis, const char* yaxis,const char* histo1des,const char* histo2des)
{


        TCanvas* canvas = new TCanvas(namecan,namecan,800,800);

        histo1->GetXaxis()->SetTitle(xaxis);
        histo1->GetXaxis()->SetTitleOffset(1.4);
        histo1->GetYaxis()->SetTitle(yaxis);
        histo1->GetYaxis()->SetTitleOffset(1.4);

        gStyle->SetOptTitle(kFALSE);
        gStyle->SetOptStat(0);

        histo1->GetXaxis()->SetLabelSize(0.045);
        histo1->SetMaximum(1.1*histo1->GetMaximum());

        histo1->SetLineColor(4);
        histo1->SetLineStyle(1);
        histo2->SetLineColor(3);
        histo2->SetLineStyle(1);

        histo1->SetMarkerStyle(56);
        histo2->SetMarkerStyle(57);

        histo1->SetMarkerSize(1.);
        histo2->SetMarkerSize(1.);

        histo1->SetMarkerColor(4);  //setting filling color
        histo2->SetMarkerColor(3);  //setting filling color

        histo1->Draw("E1 hist");
        histo2->Draw("E1 hist same");

        //TLegend* legend = new TLegend(0.65,0.66,0.85,0.82);
        TLegend* legend = new TLegend(0.2,0.75,0.4,0.85);
        legend->AddEntry(histo1,histo1des,"lep");
        legend->AddEntry(histo2,histo2des,"lep");
        legend->SetBorderSize(0);
        legend->SetBorderSize(0);
        legend->SetFillColor(0);
        legend->SetTextSize(0.037);
        legend->SetTextFont(42);
        legend->Draw();

        canvas->SaveAs(namecan,"png");
        delete canvas;

}


void analysis_compare(){

    TFile *compton = new TFile("compton_histo.root");
    TFile *mg5 = new TFile("mg5_histo.root");


    TH1 *mg5_px_a = (TH1*)mg5->Get("h_a_px");
    TH1 *mg5_py_a = (TH1*)mg5->Get("h_a_py");
    TH1 *mg5_pz_a = (TH1*)mg5->Get("h_a_pz");
    TH1 *mg5_e_a = (TH1*)mg5->Get("h_a_e");

    TH1 *mg5_px_e = (TH1*)mg5->Get("h_e_px");
    TH1 *mg5_py_e = (TH1*)mg5->Get("h_e_py");
    TH1 *mg5_pz_e = (TH1*)mg5->Get("h_e_pz");
    TH1 *mg5_e_e = (TH1*)mg5->Get("h_e_e");


    TH1 *compton_px_a = (TH1*)compton->Get("h_a_px");
    TH1 *compton_py_a = (TH1*)compton->Get("h_a_py");
    TH1 *compton_pz_a = (TH1*)compton->Get("h_a_pz");
    TH1 *compton_e_a = (TH1*)compton->Get("h_a_e");

    TH1 *compton_px_e = (TH1*)compton->Get("c_e_px");
    TH1 *compton_py_e = (TH1*)compton->Get("c_e_py");
    TH1 *compton_pz_e = (TH1*)compton->Get("c_e_pz");
    TH1 *compton_e_e = (TH1*)compton->Get("c_e_e");


    histocombo(compton_px_a,mg5_px_a, "results/photon_px.png", "Photon Px (keV)", "Counts","CompScat","MadGraph");
    histocombo(compton_py_a,mg5_py_a, "results/photon_py.png", "Photon Py (keV)", "Counts","CompScat","MadGraph");
    histocombo(compton_pz_a,mg5_pz_a, "results/photon_pz.png", "Photon Pz (keV)", "Counts","CompScat","MadGraph");
    histocombo(compton_e_a,mg5_e_a, "results/photon_energy.png", "Photon Energy (keV)", "Counts","CompScat","MadGraph");

    histocombo(compton_px_e,mg5_px_e, "results/electron_px.png", "Electron Px (keV)", "Counts","CompScat","MadGraph");
    histocombo(compton_py_e,mg5_py_e, "results/electron_py.png", "Electron Py (keV)", "Counts","CompScat","MadGraph");
    histocombo(compton_pz_e,mg5_pz_e, "results/electron_pz.png", "Electron Pz (keV)", "Counts","CompScat","MadGraph");
    histocombo(compton_e_e,mg5_e_e, "results/electron_energy.png", "Electron Energy (keV)", "Counts","CompScat","MadGraph");


}
