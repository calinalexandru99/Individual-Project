import React, {useState} from "react";
import TopBar from "../../components/TopBar";
import {AppBar, Card, List, ListItem, ListItemText, Tab, Tabs, Typography} from "@material-ui/core";
import websiteLibraries from "./websiteLibraries.json";
import algorithmPackages from "./algorithmPackages.json";
import {getPackagesArray} from "./CreditsUtils";
import {createStyles, makeStyles} from "@material-ui/core/styles";
import Panel from "../../components/Panel";

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
        appBar: {
            backgroundColor: "#EFEFEF",
        },
        tabIndicator: {
            backgroundColor: "#A9A9A9",
        },
        tab: {
            fontSize: "1rem",
        }
    })
);

const Credits: React.FC = () => {

    const classes = useStyles();

    const [currentTab, setCurrentTab] = useState(0);

    // @ts-ignore
    const onTabChange = (_event, newValue: number) => setCurrentTab(newValue);

    return (
        <>
            <TopBar showBack/>

            <AppBar className={classes.appBar} position="sticky">
                <Tabs
                    classes={{indicator: classes.tabIndicator}}
                    variant="fullWidth"
                    centered
                    aria-label="Credits pages"
                    value={currentTab}
                    onChange={onTabChange}
                >
                    <Tab className={classes.tab} label="About the website"/>

                    <Tab className={classes.tab} label="About the algorithm"/>
                </Tabs>
            </AppBar>

            <div className={classes.container}>
                <Panel value={currentTab} index={0}>
                    <Card className={classes.card}>
                        <Typography className={classes.text}>
                            The logo of the website is made by <a href="https://www.freepik.com"
                                                                  title="Freepik">Freepik</a> from <a
                            href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
                        </Typography>
                        <Typography className={classes.text}>
                            Here you can find a list of the libraries used for the creation of the website:
                        </Typography>
                        <List className={classes.list}>
                            {getPackagesArray(websiteLibraries).map(({name, version}) => (
                                <ListItem key={name}>
                                    <ListItemText primary={name} secondary={version}/>
                                </ListItem>
                            ))}
                        </List>
                    </Card>
                </Panel>

                <Panel value={currentTab} index={1}>
                    <Card className={classes.card}>
                        <Typography className={classes.text}>
                            Here you can find of list of packages used for the creation of the cross-language plagiarism
                            detection algorithm:
                        </Typography>
                        <List className={classes.list}>
                            {getPackagesArray(algorithmPackages).map(({name, version}) => (
                                <ListItem key={name}>
                                    <ListItemText primary={name} secondary={version}/>
                                </ListItem>
                            ))}
                        </List>
                    </Card>
                </Panel>
            </div>
        </>
    );
};
export default Credits;