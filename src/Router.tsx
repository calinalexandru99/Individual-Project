import React from "react";
import {createStyles, makeStyles} from "@material-ui/core/styles";
import {BrowserRouter, Route, Switch} from "react-router-dom";
import Home from "./screens/Home";

const useStyles = makeStyles(() =>
    createStyles({
        container: {
            height: "100%",
            display: "flex",
            flexDirection: "column",
        },
    })
);

const Router: React.FC = () => {

    const classes = useStyles();

    return (
        <BrowserRouter basename={process.env.PUBLIC_URL}>
            <div className={classes.container}>
                <Switch>
                    <Route exact path="/">
                        <Home/>
                    </Route>
                </Switch>
            </div>
        </BrowserRouter>
    );
};

export default Router;