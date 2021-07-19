import React, {Component} from 'react';
import './App.css';
import Header from './components/Header/Header';
import Navbar from './components/Navbar/Navbar';
import Profile from './components/Profile/Profile';
import Dialogs from "./components/Dialog/Dialogs";
import {BrowserRouter, Route} from "react-router-dom";
import Music from "./components/Music/Music";
import Settings from "./components/Settings/Settings";
import News from "./components/News/News";
import DialogsContainer from "./components/Dialog/DialogsContainer";

import UsersContainer from "./components/Users/UsersContainer";
import Userscontainer from "./components/Users/UsersContainer";
import ProfileContainer from "./components/Profile/ProfileInfo/profileContainer";
import HeaderContainer from "./components/Header/HeaderContainer";


const App = (props) => {
    return (
        <BrowserRouter>
            <div className="app-wrapper">
                <HeaderContainer/>
                <Navbar/>
                <div className="app-wrapper-content">

                    <Route path='/dialog'
                           render={() => <DialogsContainer/>}/>
                    <Route path='/profile/:userId?' render={() =>
                        <ProfileContainer/>}/>
                    <Route path='/users'
                           render={() =>
                               <UsersContainer/>}/>

                    {/*//*/}
                    {/*// /!*<Route path='/news' render={() => <News/>}/>*!/*/}
                    {/*// /!*<Route path= '/music' render ={ () => <Music/>}/>*!/*/}
                    {/*// /!*<Route path= '/settings' render = { ()=> <Settings/>}/>*!/*/}
                </div>
            </div>
        </BrowserRouter>

    )

}
export default App;
