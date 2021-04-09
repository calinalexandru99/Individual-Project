import React from "react";
import TopBar from "../../components/TopBar";
import {Button, ButtonGroup} from "@material-ui/core";
import {createStyles, makeStyles} from "@material-ui/core/styles";
import {useHistory} from "react-router-dom";
import logo from "../../misc/translate.png";

const useStyles = makeStyles((theme) =>
    createStyles({
        container: {
            height: "100%",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-evenly",
            alignItems: "center",
        },
        logo: {
            marginTop: 16,
            marginBottom: 24,
            [theme.breakpoints.down("xs")]: {
                height: 200,
            },
            [theme.breakpoints.up("sm")]: {
                height: 300,
            },
        },
        buttonsContainer: {
            width: "100%",
            display: "flex",
            justifyContent: "space-evenly",
            alignItems: "center",
        },
        button: {
            margin: 8,
            borderRadius: 20,
            fontFamily:"sans-serif",
            fontStyle:"Roboto",
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
            <TopBar/>

            <div className={classes.container}>
                <img className={classes.logo} src={logo} alt="DetecTranslation Logo"/>

                <div className={classes.buttonsContainer}>

                    <ButtonGroup orientation="vertical">
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
                </div>
            </div>
        </>
    )
}

export default Home;