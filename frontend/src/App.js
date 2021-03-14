import {
  BrowserRouter as Router,
  Route
} from "react-router-dom";
import { Navbar, Nav } from 'react-bootstrap';
import { withRouter } from "react-router";

import PrivateRoute from './Tracking/PrivateRoute';
import { AuthContext } from "./Tracking/Auth";
import useToken from './Tracking/UseToken';
import Informations from "./Tracking/Informations";

import Login from './Screens/Public/Login';
import Register from './Screens/Public/Register';
import Home from './Screens/Public/Home';
import ProfileHome from './Screens/Private/ProfileHome';
import CreationSuivi from './Screens/Private/CreationSuivi';
import Dashboard from './Screens/Private/Dashboard';
import ParametresSuivi from "./Screens/Private/ParametresSuivi";
import Reglages from './Screens/Private/Reglages';
import ChangePassword from './Screens/Private/ChangePassword';

import './App.css';


// Public Header
const PublicHeader = props => {
  const { location, token } = props;

  if (token) return null;
  
  return (
    <Navbar collapseOnSelect className='PublicNavBar' fixed="top" expand={true} bg="light">
      <Navbar.Brand >Fastocks</Navbar.Brand>
      <Navbar.Toggle aria-controls="responsive-navbar-nav" />
      <Navbar.Collapse id="responsive-navbar-nav">
      <Nav activeKey={location.pathname} className="mr-auto">
          <Nav.Link href="/">Accueil</Nav.Link>
          <Nav.Link href="/login">Se connecter</Nav.Link>
          <Nav.Link href="/register">S'inscrire</Nav.Link>
          
      </Nav>
      </Navbar.Collapse>
  </Navbar>
  );
};
const PublicHeaderWithRouter = withRouter(PublicHeader);

// Private Header 
const PrivateHeader = props => {
  const { location, token } = props;

  if (!token) return null;
  
  return (
    <Navbar collapseOnSelect className='PrivateNavBar' fixed="top" expand={true} variant='light'>
      <Navbar.Toggle aria-controls="responsive-navbar-nav" />
      <Navbar.Collapse >
        <Nav activeKey={location.pathname} className="mr-auto">
          <Nav.Item>
            <Nav.Link href="/myaccount">Accueil</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link href="/myaccount/monitor">Dashboard</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link href="/myaccount/new-monitoring">Nouveau suivi</Nav.Link>
          </Nav.Item>
          <Nav.Item>
          <Nav.Link href="/myaccount/settings">Réglages</Nav.Link>
          </Nav.Item>
        </Nav>
      </Navbar.Collapse>
  </Navbar>
  );
};
const PrivateHeaderWithRouter = withRouter(PrivateHeader);

// App
function App() {
  const {setLocalToken, setSessionToken, token } = useToken();
  const {setLocalInformations, setSessionInformations, id, phone, firstName, alertEmail, alertSms, alertPrice, alertStock } = Informations();

  return (
    <div className="Main">
      <AuthContext.Provider value={{setLocalToken, setSessionToken, token, setLocalInformations, setSessionInformations, id, phone, firstName, alertEmail, alertSms, alertPrice, alertStock }}>
        <Router>
          <PublicHeaderWithRouter token={token}/>
          <PrivateHeaderWithRouter token={token}/>
          <Route exact path="/" component={Home} />
          <Route path="/login" component={Login} />
          <Route path='/register' component={Register}/>
          <PrivateRoute exact path="/myaccount" component={ProfileHome} />
          <PrivateRoute exact path="/myaccount/settings" component={Reglages} />
          <PrivateRoute exact path="/myaccount/settings/change-password" component={ChangePassword} />
          <PrivateRoute exact path="/myaccount/new-monitoring" component={CreationSuivi} />
          <PrivateRoute exact path="/myaccount/monitor" component={Dashboard} />
          <PrivateRoute path="/myaccount/monitor/:id" component={Dashboard} />
          <PrivateRoute path="/myaccount/monitor/:id/settings" component={ParametresSuivi} />
        </Router>
      </AuthContext.Provider>
    </div>
  );
}

export default App;