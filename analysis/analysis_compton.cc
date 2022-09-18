
//using namespace std;

void analysis_compton(){

    TFile *file = new TFile("MC_compton.root");
    TTree *tree = (TTree*)file->Get("events");

    //std::vector<float> px, py, pz;
    Double_t ph_px, ph_py, ph_pz, ph_e;
    Double_t el_px, el_py, el_pz, el_e;

    tree->SetBranchAddress("Photon_Px",&ph_px);
    tree->SetBranchAddress("Photon_Py",&ph_py);
    tree->SetBranchAddress("Photon_Pz",&ph_pz);
    tree->SetBranchAddress("Photon_Energy",&ph_e);


    tree->SetBranchAddress("Electron_Px",&el_px);
    tree->SetBranchAddress("Electron_Py",&el_py);
    tree->SetBranchAddress("Electron_Pz",&el_pz);
    tree->SetBranchAddress("Electron_E",&el_e);

    TH1 *h_a_px = new TH1D("h_a_px","h_a_px",40,-1,-1);
    TH1 *h_a_py = new TH1D("h_a_py","h_a_py",40,-1,-1);
    TH1 *h_a_pz = new TH1D("h_a_pz","h_a_pz",40,-1,-1);
    TH1 *h_a_e = new TH1D("h_a_e","h_a_e",40,-1,-1);

    TH1 *h_e_px = new TH1D("c_e_px","c_e_px",40,-1,-1);
    TH1 *h_e_py = new TH1D("c_e_py","c_e_py",40,-1,-1);
    TH1 *h_e_pz = new TH1D("c_e_pz","c_e_pz",40,-1,-1);
    TH1 *h_e_e = new TH1D("c_e_e","c_e_e",40,-1,-1);


    for(int i=0; i < tree->GetEntries(); ++i){
        tree->GetEntry(i);

        h_a_px->Fill(ph_px);
        h_a_py->Fill(ph_py);
        h_a_pz->Fill(ph_pz);
        h_a_e->Fill(ph_e);
                
        h_e_px->Fill(el_px);
        h_e_py->Fill(el_py);
        h_e_pz->Fill(el_pz);
        h_e_e->Fill(el_e);
                
        

    } // for loop tree


TFile *output = new TFile("compton_histo.root","recreate");
h_a_px->Write();
h_a_py->Write();
h_a_pz->Write();
h_a_e->Write();
h_e_px->Write();
h_e_py->Write();
h_e_pz->Write();
h_e_e->Write();
output->Close();
/*

TCanvas c1;
h_a_px->Draw("hist");
c1.SaveAs("Photon_px.pdf");

h_a_py->Draw("hist");
c1.SaveAs("Photon_py.pdf");

h_a_pz->Draw("hist");
c1.SaveAs("Photon_pz.pdf");

h_a_e->Draw("hist");
c1.SaveAs("Photon_e.pdf");

// electron

h_e_px->Draw("hist");
c1.SaveAs("electron_px.pdf");

h_e_py->Draw("hist");
c1.SaveAs("electron_py.pdf");

h_e_pz->Draw("hist");
c1.SaveAs("electron_pz.pdf");

h_e_e->Draw("hist");
c1.SaveAs("electron_e.pdf");
*/


}
