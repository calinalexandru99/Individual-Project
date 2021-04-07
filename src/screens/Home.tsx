import React from "react";
import TopBar from "../components/TopBar";
import {Button, ButtonGroup} from "@material-ui/core";
import {createStyles, makeStyles} from "@material-ui/core/styles";
import {useHistory} from "react-router-dom";

const useStyles = makeStyles((theme) =>
    createStyles({
        backButton: {
            marginRight: 8,
        },
        title: {
            flexGrow: 1,
        },
        button: {
            margin: 8,
            borderRadius: 20,
            [theme.breakpoints.only("xs")]: {
                width: 250,
                fontSize: "1rem",
            },
            [theme.breakpoints.only("sm")]: {
                width: 300,
                fontSize: "1rem",
            },
            [theme.breakpoints.up("md")]: {
                width: 320,
                fontSize: "1.25rem",
            },
        },
    })
);

const Home: React.FC = () => {

    const classes = useStyles();

    const history = useHistory();

    const onMainPageClick = () => history.push("/detection");

    const onAboutClick = () => history.push("/about");

    const onCreditsClick = () => history.push("/credits");

    return (
        <>
            <TopBar>
                <ButtonGroup orientation="horizontal">
                    <Button
                        className={classes.button}
                        variant="contained"
                        color="primary"
                        size="large"
                        onClick={onMainPageClick}
                    >
                        Detect
                    </Button>

                    <Button
                        className={classes.button}
                        variant="contained"
                        color="primary"
                        size="large"
                        onClick={onAboutClick}
                    >
                        About
                    </Button>

                    <Button
                        className={classes.button}
                        variant="contained"
                        color="primary"
                        size="large"
                        onClick={onCreditsClick}
                    >
                        Credits
                    </Button>
                </ButtonGroup>
            </TopBar>
        </>
    )
}

export default Home;