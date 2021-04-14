import React from "react";
import {createStyles, makeStyles} from "@material-ui/core/styles";
import {BrowserRouter, Route, Switch} from "react-router-dom";
import Home from "./screens/Home/Home";
import Detection from "./screens/Detection/Detection";
import About from "./screens/About/About";
import Credits from "./screens/Credits/Credits";
import InvalidPage from "./screens/InvalidPage/InvalidPage";
import InputFeedback from "./screens/Detection/InputFeedback";

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

                    <Route exact path="/detection">
                        <Detection />
                    </Route>

                    <Route exact path="/detection/feedback">
                        <InputFeedback />
                    </Route>

                    <Route exact path="/about">
                        <About />
                    </Route>

                    <Route exact path="/credits">
                        <Credits />
                    </Route>

                    <Route path="/*">
                        <InvalidPage />
                    </Route>
                </Switch>
            </div>
        </BrowserRouter>
    );
};

export default Router;