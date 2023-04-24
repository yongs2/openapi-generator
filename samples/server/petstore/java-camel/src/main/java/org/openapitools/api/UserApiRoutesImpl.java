/**
* NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech) (6.6.0-SNAPSHOT).
* https://openapi-generator.tech
* Do not edit the class manually.
*/
package org.openapitools.api;

import org.apache.camel.builder.RouteBuilder;
import org.springframework.stereotype.Component;
import org.apache.camel.LoggingLevel;
import org.openapitools.model.*;
import org.apache.camel.model.dataformat.JsonLibrary;

@Component
public class UserApiRoutesImpl extends RouteBuilder {
    @Override
    public void configure() throws Exception {
        
        /**
        POST /user : Create user
        **/
        from("direct:createUser")
            .id("createUser")
            .choice()
                .when(simple("${body} != null"))
                    .log(LoggingLevel.INFO, "BODY TYPE: ${body.getClass().getName()}")
            .end()
            .log(LoggingLevel.INFO, "HEADERS: ${headers}");
        /**
        POST /user/createWithArray : Creates list of users with given input array
        **/
        from("direct:createUsersWithArrayInput")
            .id("createUsersWithArrayInput")
            .choice()
                .when(simple("${body} != null"))
                    .log(LoggingLevel.INFO, "BODY TYPE: ${body.getClass().getName()}")
            .end()
            .log(LoggingLevel.INFO, "HEADERS: ${headers}");
        /**
        POST /user/createWithList : Creates list of users with given input array
        **/
        from("direct:createUsersWithListInput")
            .id("createUsersWithListInput")
            .choice()
                .when(simple("${body} != null"))
                    .log(LoggingLevel.INFO, "BODY TYPE: ${body.getClass().getName()}")
            .end()
            .log(LoggingLevel.INFO, "HEADERS: ${headers}");
        /**
        DELETE /user/{username} : Delete user
        **/
        from("direct:deleteUser")
            .id("deleteUser")
            .choice()
                .when(simple("${body} != null"))
                    .log(LoggingLevel.INFO, "BODY TYPE: ${body.getClass().getName()}")
            .end()
            .log(LoggingLevel.INFO, "HEADERS: ${headers}");
        /**
        GET /user/{username} : Get user by user name
        **/
        from("direct:getUserByName")
            .id("getUserByName")
            .choice()
                .when(simple("${body} != null"))
                    .log(LoggingLevel.INFO, "BODY TYPE: ${body.getClass().getName()}")
            .end()
            .log(LoggingLevel.INFO, "HEADERS: ${headers}")
            .setBody(constant("{ \"firstName\" : \"firstName\", \"lastName\" : \"lastName\", \"password\" : \"password\", \"userStatus\" : 6, \"phone\" : \"phone\", \"id\" : 0, \"email\" : \"email\", \"username\" : \"username\" }"))
            .unmarshal().json(JsonLibrary.Jackson, User.class);
        /**
        GET /user/login : Logs user into the system
        **/
        from("direct:loginUser")
            .id("loginUser")
            .choice()
                .when(simple("${body} != null"))
                    .log(LoggingLevel.INFO, "BODY TYPE: ${body.getClass().getName()}")
            .end()
            .log(LoggingLevel.INFO, "HEADERS: ${headers}");
        /**
        GET /user/logout : Logs out current logged in user session
        **/
        from("direct:logoutUser")
            .id("logoutUser")
            .choice()
                .when(simple("${body} != null"))
                    .log(LoggingLevel.INFO, "BODY TYPE: ${body.getClass().getName()}")
            .end()
            .log(LoggingLevel.INFO, "HEADERS: ${headers}");
        /**
        PUT /user/{username} : Updated user
        **/
        from("direct:updateUser")
            .id("updateUser")
            .choice()
                .when(simple("${body} != null"))
                    .log(LoggingLevel.INFO, "BODY TYPE: ${body.getClass().getName()}")
            .end()
            .log(LoggingLevel.INFO, "HEADERS: ${headers}");
    }
}
