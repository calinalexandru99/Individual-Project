import React from "react";
import TopBar from "../../components/TopBar";
import {Button, Card, Typography} from "@material-ui/core";
import {createStyles, makeStyles} from "@material-ui/core/styles";
import imperial from "../../misc/imperial.png"
import {useHistory} from "react-router-dom";

const useStyles = makeStyles((theme) =>
    createStyles({
        card: {
            height: "80%",
            width: "80%",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-evenly",
            padding: 8,
        },
        text: {
            textAlign: "center",
            [theme.breakpoints.only("xs")]: {
                fontSize: "1rem",
            },
            [theme.breakpoints.only("sm")]: {
                fontSize: "1.25rem",
            },
            [theme.breakpoints.only("md")]: {
                fontSize: "1.5rem",
            },
            [theme.breakpoints.up("lg")]: {
                fontSize: "2rem",
            },
        },
        container: {
            marginTop: "50px",
            flex: 1,
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-evenly",
            alignItems: "center",
        },
        imageContainer: {
            display: "flex",
            flexDirection: "row",
            justifyContent: "space-between",
            justifyItems: "center",
            alignItems: "center",
            marginLeft: "40%",
        },
        image: {
            [theme.breakpoints.down("xs")]: {
                width: "90%",
            },
            [theme.breakpoints.only("sm")]: {
                width: "70%",
            },
            [theme.breakpoints.up("md")]: {
                width: "70%",
            },
        },
        button: {
            marginLeft: "38%",
            margin: 8,
            borderRadius: 20,
            fontFamily: "sans-serif",
            fontStyle: "Roboto",
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

const About: React.FC = () => {

    const classes = useStyles();

    const history = useHistory();

    const onButtonClick = () => history.replace("/detection");

    return (
        <>
            <TopBar showBack/>
            <div className={classes.container}>
                <Card className={classes.card}>

                    <Typography className={classes.text}>
                        This website is part of a 3rd Year Individual Project at Imperial College London. The supervisor
                        of this project is Dr. Thomas Lancaster.
                    </Typography>

                    <div className={classes.imageContainer}>
                        <a href="http://www.imperial.ac.uk/" target="blank">
                            <img className={classes.image} src={imperial} alt={imperial}/>
                        </a>
                    </div>

                    <Typography className={classes.text}>
                        This website was created with React by Calin-Andrei Alexandru, a 3rd Year Computing student at
                        Imperial College London. The purpose of this website is to showcase the detection of
                        automatically
                        translated documents algorithm described in the Individual Project report. The report can be
                        viewed by downloading the following file:
                        <a href={"Project_Report.pdf"} download>
                            Report.pdf
                        </a>
                    </Typography>

                    <Typography className={classes.text}>
                        The algorithm is showcased in the Detection tab, where one can check if a piece of text has been
                        cross-language plagiarized or not.
                    </Typography>

                    <Button
                        className={classes.button}
                        variant="contained"
                        color="primary"
                        size="large"
                        onClick={onButtonClick}
                    >
                        Go to Detection tab
                    </Button>

                </Card>
            </div>
        </>
    );
};
export default About;