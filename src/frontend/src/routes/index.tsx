import {
    BrowserRouter,
    Routes,
    Route,

    // Navigate
} from 'react-router-dom'

import HomePage from './home'

import PageNotFound from './pageNotFound'


export default function Router(){
    return <BrowserRouter basename='/'>
        <Routes>
            <Route path="/">
                <Route index element={<HomePage/>}/>
                <Route path="recipes" element={null}/>
                <Route path="recipe">
                    <Route index element={null}/>
                    <Route path=":recipeId" element={null}/>
                </Route>
                <Route path="*" element={<PageNotFound/>}/>
            </Route>
        </Routes>
    </BrowserRouter>
}
