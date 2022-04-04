import {
    BrowserRouter,
    Routes,
    Route,

    Navigate
} from 'react-router-dom'

import HomePage from './home'

import PageNotFound from './pageNotFound'


export default function Router(){
    return <BrowserRouter basename='/'>
        <Routes>
            <Route path="/">
                {/* homepage */}
                <Route index element={<HomePage/>}/>
                {/* infinite scroll of recipes */}
                <Route path="recipes" element={null}/>
                {/* direct view of recipes */}
                <Route path="recipe">
                    <Route index element={null}/>
                    <Route path=":recipeId" element={null}/>
                </Route>
                {/* about users */}
                <Route path="user">
                    <Route index element={<Navigate to="me"/>}/>
                    {/* show info about logged in user (mayber same view as with :userId but missing userId gets replaced with User.userId) */}
                    <Route path="me" element={null}/>
                    {/* show a user by id (maybe by name) */}
                    <Route path=":userId" element={null}/>
                </Route>
                <Route path="*" element={<PageNotFound/>}/>
            </Route>
        </Routes>
    </BrowserRouter>
}
