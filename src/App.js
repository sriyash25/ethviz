import { useState } from "react";
import { Routes, Route } from "react-router-dom";
import { ProSidebarProvider } from 'react-pro-sidebar';
// import Topbar from "./scenes/global/Topbar";
import Mysidebar from "./scenes/global/Sidebar";
import Dashboard from "./scenes/dashboard";
// import Team from "./scenes/team";
// import Invoices from "./scenes/invoices";
// import Contacts from "./scenes/contacts";
// import Bar from "./scenes/bar";
// import Form from "./scenes/form";
// import Line from "./scenes/line";
// import Pie from "./scenes/pie";
// import FAQ from "./scenes/faq";
import Geography from "./scenes/geography";
import MapChart from "./components/MapChart";
import ElectricityChart from "./components/ElectricityChart";
import DistanceChart from "./components/DistanceChart";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { ColorModeContext, useMode } from "./theme";
import AppGraph from "./AppGraph";
// import Calendar from "./scenes/calendar/calendar";

function App() {
  const [theme, colorMode] = useMode();
  const [isSidebar, setIsSidebar] = useState(true);

  return (
    
    <ColorModeContext.Provider value={colorMode}>
      <ProSidebarProvider>
      <ThemeProvider theme={theme}>    
        <CssBaseline />
        <div className="app">
          <Mysidebar isSidebar={isSidebar} />
          <main className="content">
            {/* <Topbar setIsSidebar={setIsSidebar} /> */}
            <Routes>
              <Route path="/" element={<Dashboard />} />
              {/* <Route path="/team" element={<Team />} />
              <Route path="/contacts" element={<Contacts />} />
              <Route path="/invoices" element={<Invoices />} />
              <Route path="/form" element={<Form />} />
              <Route path="/bar" element={<Bar />} />
              <Route path="/pie" element={<Pie />} />
              <Route path="/line" element={<Line />} />
              <Route path="/faq" element={<FAQ />} />
              <Route path="/calendar" element={<Calendar />} /> */}
              <Route path="/chart" element={<DistanceChart />} />
              <Route path="/geography" element={<MapChart />} />
              <Route path="/electricity" element={<ElectricityChart />} />
              <Route path="/privatechain" element={<AppGraph />} />
            </Routes>
          </main>
        </div>
      </ThemeProvider>
      </ProSidebarProvider>
    </ColorModeContext.Provider>
    
  );
}

export default App;






