import React from "react";
import TopBar from "../../components/TopBar";
import {Card, List, ListItem, ListItemText, Typography} from "@material-ui/core";
import libraries from "./libraries.json";
import {getPackagesArray} from "./CreditsUtils";
import {createStyles, makeStyles} from "@material-ui/core/styles";

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
        list: {
            flex: 1,
            height: 0,
            overflow: "auto",
        },
        container: {
            marginTop: "50px",
            flex: 1,
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",
        },
    })
);

const Credits: React.FC = () => {

    const classes = useStyles();

    return (
        <>
            <TopBar showBack/>
            <div className={classes.container}>
                <Card className={classes.card}>
                    <Typography className={classes.text}>
                        Here is a list of libraries and images used, kudos to the creators for enabling us to
                        work effectively.
                    </Typography>

                    <Typography className={classes.text}>
                        You can find a link to the authors and the licenses for the images by clicking here:{" "}

                    </Typography>
                    <Typography className={classes.text}>
                        Here are the libraries that this game uses:
                    </Typography>
                    <List className={classes.list}>
                        {getPackagesArray(libraries).map(({name, version}) => (
                            <ListItem key={name}>
                                <ListItemText primary={name} secondary={version}/>
                            </ListItem>
                        ))}
                    </List>
                </Card>
            </div>
        </>
    );
};
export default Credits;